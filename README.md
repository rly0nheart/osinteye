![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rly0nheart/osinteye?style=flat&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/osinteye?style=flat&logo=github)

> Username enumeration & reconnaisance suite
![osinteye](https://user-images.githubusercontent.com/74001397/155044129-24ace3c3-5ffb-407d-a49a-2c3f5c4da479.gif)


# Supported sites
* PyPI
* Github
* TestPypi
* About.me
* Instagram
* DockerHub


# Installation
> ![osinteye](https://user-images.githubusercontent.com/74001397/155046090-ac5c4943-d8bb-46e2-8dd3-21f94338febf.gif)

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
$ python osinteye [--SITENAME] [USERNAME]
```

**Or give osintEye execution permission**:
```
$ chmod +x osinteye
```

```
$ ./osinteye [--SITENAME] [USERNAME]
```

**Example 1.1**;
```
$ python osinteye --instagram [USERNAME]
```

**Example 1.2**;
```
$ ./osinteye --instagram [USERNAME]
```

# Optional Arguments
| Flag        | Usage |
| ------------- |:---------:|
| <code>--pypi</code> |  *get target's information from pypi*  |
| <code>--testpypi</code> |  *get target's information from testpypi*  |
| <code>--about</code> |  *get target's information from about.me*  |
| <code>--instagram</code> |  *get target's information from instagram*  |
| <code>--github</code> |  *get target's information from github*  |
| <code>--dockerhub</code> |  *get target's information from dockerhub*  |
| <code>-v/--verbose</code>  | *enable verbosity (returns network logs, errors and warnings)*  |
| <code>--version</code> |  *show program's version number and exit*  |

# LICENSE
![license](https://user-images.githubusercontent.com/74001397/137917929-2f2cdb0c-4d1d-4e4b-9f0d-e01589e027b5.png)

# About me
* [About.me](https://about.me/rly0nheart)
