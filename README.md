# echo-encode-file
A tool to pack a file as echo commands

# About

Compile a provided example:

```
gcc -Os -s hello.c
```

Encode it:

```
./encode.py > sample.sh
```


Transfer the resulted script file into another machine over an ssh terminal, or a serial console or whatever way that has restriction for printable only symbols. Run it:

```
chmod +x sample.sh 
./sample.sh 
md5sum a.out b.out 
40c83a102b1785f991d92e42f7c858f3  a.out
40c83a102b1785f991d92e42f7c858f3  b.out
```

It will produce the same file
