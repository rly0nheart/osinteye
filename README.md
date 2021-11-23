![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/osinteye?style=flat&logo=github)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/osinteye/badge)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/rlyonheart/osinteye?style=flat&logo=github)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/osinteye?style=flat&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/osinteye?style=flat&logo=github)

A 👥user 🔎reconnaisance tool that extracts a ⭕target's information from Instagram, DockerHub &amp; Github. Also 🔎searches for matching usernames on Github.
![osinteye](https://user-images.githubusercontent.com/74001397/143137199-d3545457-7b78-48d5-9d9d-e6d2623b4a47.gif)


# Features
* extracts Instagram info
* extracts DockerHub info
* extracts Github info (including followers list and repositories)
* searches related usernames on Github


# Installation
Clone project:

```
git clone https:/github.com/rlyonheart/osinteye.git
```

```
cd osinteye
```

```
pip install -r requirements.txt
```

# Usage
```
python osinteye --[SITENAME] [USERNAME]
```

**Or give osintEye execution permission**:
```
chmod +x osinteye
```

```
./osinteye --[SITENAME] [USERNAME]
```

**Example .1**;
```
python osinteye --instagram johndoe
```

**Example .2**;
```
./osinteye --instagram johndoe
```

# Available Sources
* Instagram
* DockerHub
* Github

| Flag        | Usage |
| ------------- |:---------:|
| <code>-I/--instagram</code> |  *get target's Instagram information*  |
| <code>-G/--github</code> |  *get target's Github information*  |
| <code>-D/--dockerhub</code> |  *get target's DockerHub information*  |
| <code>-X/--all</code> |  *get target's information from all available sources*  |

# Optional Arguments
| Flag         | Usage|
| ------------- |:---------:|
| <code>-sG/--github-search</code> | *search username on Github* |
| <code>-r/--raw</code> | *return output in raw json format*  |
| <code>-v/--verbose</code>  | *run osintEye in verbose mode (returns network logs, errors and warnings)*  |


# Disclaimer
*This tool should not be used in environments withouth legal authorization.
The author [Richard Mwewa](https://about.me/rlyonheart) will not be responsible for the damages that might be done with it.**

# LICENSE
![license](https://user-images.githubusercontent.com/74001397/137917929-2f2cdb0c-4d1d-4e4b-9f0d-e01589e027b5.png)

# About author
* [About.me](https://about.me/rlyonheart)

# Contact author
* [Github](https://github.com/rlyonheart)

* [Twitter](https://twitter.com/rly0nheart)
