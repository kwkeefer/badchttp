# badchars

A very small app that generates sequential characters over HTTP.

Simply append bad characters to the URL to remove them.

### Run

```shell
python3 badchars.py
```

### Use

Create a sequential bytes string without `\x0a` and `\x0d` (`\x00` is removed by default).

```shell
curl -o chars.txt http://localhost:5000/x0a/x0d 
```

If that the forward slash feels wrong the backslash should work too. Just make sure to include the initial forward slash
after the port.

```shell
curl -o chars.txt http://localhost:5000/\x0a\x0d
```
