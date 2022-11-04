# badchttp

badchttp is a small flask app that makes it easier to identify bad characters for buffer overflow exploitation.  Created during my OSCP studies.  

### Usage 

Simply run `badchttp` to start the app

```shell
curl -o chars.txt http://localhost:1337/x0a/x0d 
```
Creates a sequential bytes string without `\x0a` and `\x0d` 

If that the forward slash feels wrong the backslash should work too. Just make sure to include the initial forward slash
after the port:

```shell
curl -o chars.txt http://localhost:5000/\x0a\x0d
```


### Installation Method #1: pipx (Recommended)

It is recommended you use `pipx` to install badchttp. pipx will install badchttp in it's own virtual environment, and make it available in the global context, avoiding conflicting package dependencies and the resulting instability. First, install pipx using the following commands:


```bash
sudo apt install python3-venv
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

You will have to re-source your ~/.bashrc or ~/.zshrc file (or open a new tab) after running these commands in order to use pipx.

Install badchttp using the following command:

```bash
pipx install git+https://github.com/kwkeefer/badchttp.git
```

### Installation Method #2: pip

Alternatively you can use `pip` to install badchttp using the following command:

```bash
python3 -m pip install git+https://github.com/kwkeefer/badchttp.git
```

