from utils import ensure_dirs, RESULTS, log

def collect():
    ensure_dirs()
    files = sorted(RESULTS.glob("*.txt"))
    total = 0
    count = 0

    for f in files:
        txt = f.read_text(encoding="utf-8").strip().splitlines()
        for line in txt:
            if line.startswith("result="):
                total += int(line.split("=", 1)[1])
                count += 1

    log(f"COLLECTOR read {count} results, sum={total}")
    print(f"Collected results: {count} files, sum(result)={total}")

if __name__ == "__main__":
    collect()