import os

LINE = "Sorry I jammed on your big report. You feed me bargain paper, swear at me in two languages, and still expect colour."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
