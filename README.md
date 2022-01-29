![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rly0nheart/osinteye?style=flat&logo=github)
![CodeFactor](https://www.codefactor.io/repository/github/rly0nheart/osinteye/badge)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/rly0nheart/osinteye?style=flat&logo=github)
![Lines of code](https://img.shields.io/tokei/lines/github/rly0nheart/osinteye?style=flat&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/osinteye?style=flat&logo=github)

A 👥user 🔎reconnaisance tool that extracts a information from About.me, Instagram, DockerHub &amp; Github.
![osinteye](https://user-images.githubusercontent.com/74001397/143137199-d3545457-7b78-48d5-9d9d-e6d2623b4a47.gif)


# Features
* extracts About.me
* extracts Instagram info
* extracts DockerHub info
* extracts Github info (including repositories)


# Installation
![installation](https://user-images.githubusercontent.com/74001397/143138986-c0cf6065-942b-4276-b917-c0bfb17b2a9d.gif)

Clone project:

```
$ git clone https://github.com/rly0nheart/osinteye.git
```

```
$ cd osinteye
```

```
$ pip install -r requirements.txt
```

# Usage
```
$ python osinteye [SITENAME] [USERNAME]
```

**Or give osintEye execution permission**:
```
$ chmod +x osinteye
```

```
$ ./osinteye --[SITENAME] [USERNAME]
```

**Example 1.1**;
```
$ python osinteye --instagram username
```

**Example 1.2**;
```
$ ./osinteye --instagram username
```

# Available Sources
* Github
* About.me
* Instagram
* DockerHub

# Optional Arguments
| Flag        | Usage |
| ------------- |:---------:|
| <code>--about</code> |  *[OPTIONAL] get target's About.me information*  |
| <code>--instagram</code> |  *[OPTIONAL] get target's Instagram information*  |
| <code>--github</code> |  *[OPTIONAL] get target's Github information*  |
| <code>--dockerhub</code> |  *[OPTIONAL] get target's DockerHub information*  |
| <code>-v/--verbose</code>  | *[RECOMMENDED] enable verbosity (returns network logs, errors and warnings)*  |
| <code>--version</code> |  *[OPTIONAL] show program's version number and exit*  |

# LICENSE
![license](https://user-images.githubusercontent.com/74001397/137917929-2f2cdb0c-4d1d-4e4b-9f0d-e01589e027b5.png)

# About me
* [About.me](https://about.me/rly0nheart)
