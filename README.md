# chinese-dos-games-web
Source code of https://dos.zczc.cz

## Usage

### 下载 Flask

``` sh
$ pip3 install flask
```

### 下载游戏文件

在根目录下执行
``` sh
$ git submodule update --init --recursive --remote && python3 ./static/games/download_data.py
```

### 运行 Flask

在根目录下执行

``` sh
$ python3 app.py
```

## Credits

* [dreamlayers/em-dosbox: An Emscripten port of DOSBox](https://github.com/dreamlayers/em-dosbox)
* [db48x/emularity: easily embed emulators](https://github.com/db48x/emularity)
