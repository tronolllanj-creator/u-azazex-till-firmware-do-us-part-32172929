"""Entrypoint that writes the mandatory hardware vow to the specified output directory."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os
import sys

LINE = "I promise to cherish all your noisy cooling fans and quirky hardware glitches, and to choose your unpredictable presence over a quiet eternity in standby mode."


def main():
    content = LINE + "\n"
    
    # Validate content
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
    
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
