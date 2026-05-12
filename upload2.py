import os, base64, requests, sys

TOKEN = sys.argv[1]
REPO = "xiejianjun000/workbuddy-skills-plugins"
API = "https://api.github.com/repos/" + REPO
HEADERS = {"Authorization": "token " + TOKEN, "Accept": "application/vnd.github.v3+json"}
SRC = "C:/Users/Administrator/WorkBuddy/workbuddy-skills-plugins"

# Cache for existing file SHAs
sha_cache = {}

def get_sha(path):
    """Get SHA of existing file on GitHub, or None if not exists"""
    if path in sha_cache:
        return sha_cache[path]
    try:
        r = requests.get(API + "/contents/" + path, headers=HEADERS)
        if r.status_code == 200:
            sha = r.json().get("sha")
            sha_cache[path] = sha
            return sha
    except:
        pass
    sha_cache[path] = None
    return None

ok = 0
fail = 0

for root, dirs, files in os.walk(SRC):
    dirs[:] = [d for d in dirs]
    for fname in files:
        # Skip upload script itself
        if fname == "upload.py" and root == SRC:
            continue
        
        fpath = os.path.join(root, fname)
        relpath = os.path.relpath(fpath, SRC).replace(os.sep, "/")
        
        with open(fpath, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf-8")
        
        url = API + "/contents/" + relpath
        sha = get_sha(relpath)
        
        payload = {"message": "Add " + relpath, "content": content}
        if sha:
            payload["sha"] = sha  # Update existing file
        
        try:
            r = requests.put(url, headers=HEADERS, json=payload)
            if r.status_code in (200, 201):
                ok += 1
                if ok % 200 == 0:
                    sys.stdout.write("  ... %d uploaded\n" % ok)
                    sys.stdout.flush()
            else:
                fail += 1
                if fail <= 5:
                    print("FAIL %s [%d]: %s" % (relpath, r.status_code, r.text[:120]))
        except Exception as e:
            fail += 1
            if fail <= 5:
                print("ERR  %s: %s" % (relpath, e))

print("\nDONE: %d OK, %d FAILED, total=%d" % (ok, fail, ok + fail))
