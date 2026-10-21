<div align="center">
<h1>GITSINT</h1>
</div>
<img alt="" src="https://raw.githubusercontent.com/FatalS3C/gitsint/refs/heads/main/images/logo.png" />

**GITSINT** is an osint tool for GitHub repositories and profiles, written in Python 3.
<div align="center">
<a target="_blank"><img alt='redhat' src='https://img.shields.io/badge/OsinT-100000?style=for-the-badge&logo=redhat&logoColor=white&labelColor=black&color=black'/></a>
<a href='https://www.python.org/downloads/' target="_blank"><img alt='python' src='https://img.shields.io/badge/python_3-100000?style=for-the-badge&logo=python&logoColor=white&labelColor=black&color=black'/></a>
</div>


**Developed by:** [@Fatalsec](https://t.me/fatalsec)

---

## Features

- **Full Profile Scan (`--get`)** — Collects profile information, repositories, and commits associated with those repositories.
- **Simple Profile Scan (`--simple`)** — Retrieves basic profile information without performing a full scan.
- **Commit Analysis (`--commit`)** — Inspects a specific commit to collect available information, including additional commit details.
- **Repository Analysis (`--repo`)** — Collects relevant repository information and inspects its commits.

## Examples
<figure align="center">
  <img src="https://raw.githubusercontent.com/FatalS3C/gitsint/refs/heads/main/images/print2.png"" alt="example" width="800">
  <figcaption><i>Full Profile Scan</i> <b>python3 gitsint.py --get https://github.com/FatalS3C</b></figcaption>
</figure>

<figure align="center">
  <img src="https://raw.githubusercontent.com/FatalS3C/gitsint/refs/heads/main/images/print4.png" alt="example" width="800">
  <figcaption><i>Simple profile scan</i> <b>python3 gitsint.py --simple https://github.com/FatalS3C</b></figcaption>
</figure>

<figure align="center">
  <img src="https://raw.githubusercontent.com/FatalS3C/gitsint/refs/heads/main/images/print3.png" alt="example" width="800">
  <figcaption><i>Repo scan</i> <b>python3 gitsint.py --repo https://github.com/FatalS3C/gitsint/</b></figcaption>
</figure>

<figure align="center">
  <img src="https://raw.githubusercontent.com/FatalS3C/gitsint/refs/heads/main/images/print1.png" alt="example" width="800">
  <figcaption><i>Commit scan</i> <b>python3 gitsint.py --commit https://github.com/FatalS3C/gitsint/commit/e850e892994b7caebf94b39219872accd752d837</b></figcaption>
</figure>

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

<a href='https://t.me/fatalsec' target="_blank"><img alt='telegram' src='https://img.shields.io/badge/My_channel-100000?style=for-the-badge&logo=telegram&logoColor=white&labelColor=black&color=black'/></a>
<a href='https://www.instagram.com/fatalsec/' target="_blank"><img alt='instagram' src='https://img.shields.io/badge/Instagram-100000?style=for-the-badge&logo=instagram&logoColor=white&labelColor=black&color=black'/></a>
<a href='https://www.youtube.com/@fatalsecarchon' target="_blank"><img alt='youtube' src='https://img.shields.io/badge/youtube-100000?style=for-the-badge&logo=youtube&logoColor=white&labelColor=black&color=black'/></a>

## My community (Brazuka Undernet)

<a href='https://brazukaundernet.pages.dev/' target="_blank"><img alt='dpd' src='https://img.shields.io/badge/Brazukaundernet_site-100000?style=for-the-badge&logo=dpd&logoColor=white&labelColor=E71B1B&color=B30303'/></a>
<a href='https://t.me/brazuka_undernet' target="_blank"><img alt='telegram' src='https://img.shields.io/badge/Brazukaundernet_teleram-100000?style=for-the-badge&logo=telegram&logoColor=white&labelColor=E71B1B&color=B30303'/></a>

<p><i>The community is Brazilian, so it might be difficult to communicate in another language.</i></p>
---

<p align="center">
  <i>GitSint — Inspect the profile. Explore & Investigate.</i>
</p>
