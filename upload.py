import os, base64, requests, sys, time

TOKEN = sys.argv[1]
REPO = "xiejianjun000/workbuddy-skills-plugins"
BASE = f"https://api.github.com/repos/{REPO}/contents"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

SRC = "C:/Users/Administrator/WorkBuddy/workbuddy-skills-plugins"

ok = 0
fail = 0

def upload_file(filepath, relpath):
    global ok, fail
    with open(filepath, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")
    url = f"{BASE}/{relpath}"
    data = {"message": f"Add {relpath}", "content": content}
    try:
        r = requests.put(url, headers=HEADERS, json=data)
        if r.status_code in [200, 201]:
            ok += 1
            if ok % 100 == 0:
                print(f"  ... {ok} uploaded so far")
        else:
            fail += 1
            if r.status_code != 422:  # skip duplicate errors in summary
                print(f"FAIL {relpath} [{r.status_code}]")
    except Exception as e:
        fail += 1
        print(f"ERR  {relpath}: {e}")

# Upload README first
readme = os.path.join(SRC, "README.md")
if os.path.exists(readme):
    upload_file(readme, "README.md")
    print(f"OK README.md ({ok} done)")

# Upload all plugin files
for root, dirs, files in os.walk(SRC):
    # Skip README (already uploaded)
    dirs[:] = [d for d in dirs]
    for fname in files:
        if fname == "README.md" and root == SRC:
            continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, SRC).replace("\\", "/")
        upload_file(fpath, rel)

print(f"\nDONE: {ok} OK, {fail} FAILED out of {ok + fail}")
