# GitSint

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Cross--platform-222222?style=for-the-badge&logo=linux&logoColor=white" alt="Platform">
  <img src="https://img.shields.io/badge/Focus-GitHub%20OSINT-FF3333?style=for-the-badge&logo=github&logoColor=white" alt="GitHub OSINT">
</p>


<img src="https://raw.githubusercontent.com/FatalS3C/gitsint/refs/heads/main/ascii-magic-1.gif">
**GitSint** It's an OSINT tool for GitHub, written in Python 3.

It provides four analysis modes, ranging from quick profile lookups to comprehensive profile scans covering repositories and their commits. It also supports inspecting individual repositories and commits for additional information, including details that may not be immediately visible in standard GitHub pages.

> osint tool for Github

**Developed by:** [@Fatalsec](https://t.me/fatalsec)

---

## Features

- **Full Profile Scan (`--get`)** — Collects profile information, repositories, and commits associated with those repositories.
- **Simple Profile Scan (`--simple`)** — Retrieves basic profile information without performing a full scan.
- **Commit Analysis (`--commit`)** — Inspects a specific commit to collect available information, including additional commit details.
- **Repository Analysis (`--repo`)** — Collects relevant repository information and inspects its commits.

## Requirements

- Python 3


## Installation

Clone the repository:

```bash
git clone https://github.com/FatalS3C/gitsint.git
cd gitsint
```


## Usage

```bash
python3 gitsint.py --help
```

Output:

```text
usage: gitsint.py [-h] [--get GITHUB-LINK] [--simple GITHUB-LINK]
                  [--commit GITHUB-COMMIT-LINK] [--repo GITHUB-REPO-LINK]

options:
  -h, --help            show this help message and exit
  --get GITHUB-LINK     Perform a full profile scan
  --simple GITHUB-LINK  Simple profile scan
  --commit GITHUB-COMMIT-LINK
                        Simple commit parse
  --repo GITHUB-REPO-LINK
                        Simple repo parse
```

## Analysis Modes

### 1. Full Profile Scan — `--get`

Performs a comprehensive scan of a GitHub profile, collecting profile information, repositories, and commits associated with those repositories.

```bash
python3 gitsint.py --get https://github.com/USER/
```

**Use it when:** You want to explore a profile and gather information across its repositories and commit history.

### 2. Simple Profile Scan — `--simple`

Performs a quick lookup of a GitHub profile, focusing on basic account information.

```bash
python3 gitsint.py --simple https://github.com/USER/
```

**Use it when:** You need a quick overview of a profile without running a comprehensive scan.

### 3. Commit Analysis — `--commit`

Inspects a specific GitHub commit and collects available information associated with it.

```bash
python3 gitsint.py --commit https://github.com/USER/REPO/commit/HASH
```

**Use it when:** You want to investigate a particular commit and examine its available details.

### 4. Repository Analysis — `--repo`

Analyzes a GitHub repository, collecting relevant repository information and inspecting its commits.

```bash
python3 gitsint.py --repo https://github.com/USER/REPO/
```

**Use it when:** You want to explore a repository and gather information about its development history.

## Technologies

GitSint is built with Python 3 and uses the following libraries:

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| BeautifulSoup 4 | HTML parsing and data extraction |
| Requests | HTTP requests |
| urllib | URL handling and standard-library HTTP utilities |

## Disclaimer

GitSint is intended for educational purposes, research, and authorized security investigations.

Use this tool responsibly and respect GitHub's terms of service, applicable laws, and the privacy of others. Only use collected information in ways you are authorized to.

The user is responsible for how the tool is used.

## Author

**USER**

- Telegram: [@fatalsec](https://t.me/fatalsec)
- GitHub: [@USER](https://github.com/FatalS3C)

---

<p align="center">
  <i>GitSint — Inspect the profile. Explore & Investigate.</i>
</p>
