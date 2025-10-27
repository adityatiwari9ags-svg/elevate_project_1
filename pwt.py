
import re, argparse, math
from datetime import datetime

# ---------- Password Analyzer ----------
def entropy(password: str) -> float:
    """Rough entropy calculation."""
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^A-Za-z0-9]', password): charset += 32
    if charset == 0: return 0
    return len(password) * math.log2(charset)

def analyze_password(pw: str):
    e = entropy(pw)
    if e < 28: level = "Very Weak"
    elif e < 36: level = "Weak"
    elif e < 60: level = "Moderate"
    elif e < 90: level = "Strong"
    else: level = "Very Strong"
    print(f"\nPassword Analysis:")
    print(f"  Entropy: {e:.2f} bits")
    print(f"  Strength: {level}\n")

# ---------- Wordlist Generator ----------
LEET = {'a':['4','@'], 'e':['3'], 'i':['1'], 'o':['0'], 's':['5'], 't':['7']}
SUFFIXES = ['', '123', '!', '@', '007']
PREFIXES = ['', 'my', 'the']

def leet_variants(word):
    variants = {word}
    for i,c in enumerate(word.lower()):
        if c in LEET:
            for rep in LEET[c]:
                variants.add(word[:i] + rep + word[i+1:])
    return variants

def generate_words(bases, years):
    seen = set()
    for base in bases:
        base = base.strip()
        if not base: continue
        variants = set([base, base.lower(), base.upper(), base.capitalize(), base[::-1]])
        for v in list(variants):
            variants |= leet_variants(v)
        for v in variants:
            for pre in PREFIXES:
                for suf in SUFFIXES:
                    word = f"{pre}{v}{suf}"
                    if word not in seen:
                        seen.add(word)
                        yield word
                    for y in years:
                        for w2 in (f"{word}{y}", f"{y}{word}"):
                            if w2 not in seen:
                                seen.add(w2)
                                yield w2

def parse_dates(datestr):
    years = set()
    if not datestr: return years
    for d in datestr.split(','):
        d = d.strip()
        if re.fullmatch(r'\d{4}', d): years.add(d)
        else:
            nums = re.findall(r'\d{4}', d)
            years.update(nums)
    return years

def main():
    p = argparse.ArgumentParser(description="Simple Password Strength Analyzer + Wordlist Generator")
    p.add_argument("--name", default="", help="Comma-separated names")
    p.add_argument("--pet", default="", help="Comma-separated pets")
    p.add_argument("--dates", default="", help="Comma-separated years/dates")
    p.add_argument("--phrases", default="", help="Comma-separated phrases")
    p.add_argument("--testpass", default=None, help="Password to test strength")
    p.add_argument("--output", default="wordlist.txt", help="Output filename")
    p.add_argument("--limit", type=int, default=5000, help="Maximum words")
    args = p.parse_args()

    if args.testpass:
        analyze_password(args.testpass)

    tokens = set()
    for s in (args.name, args.pet, args.phrases):
        for part in s.split(','):
            part = re.sub(r'\W+', '', part)
            if part: tokens.add(part)
    years = parse_dates(args.dates)
    if not tokens: tokens.add("default")

    print(f"Generating wordlist from {len(tokens)} base words, years={years}")
    with open(args.output, "w", encoding="utf-8") as f:
        count = 0
        for w in generate_words(tokens, years):
            f.write(w + "\n")
            count += 1
            if count >= args.limit: break
    print(f"Saved {count} words → {args.output}")

if __name__ == "__main__":
    main()