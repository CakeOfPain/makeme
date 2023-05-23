
# MAKEME Project

`makeme` is a build tool that automates the installation and setup process based on the instructions provided in the README file. It is designed to simplify the build workflow by executing commands.

Use `makeme` for your project to simplify the setup process and installation. You can also add custom commands to your project, like run, test, etc.

If you use `makeme` for your project the README will be actively used and therefore maintained. 

## License
`makeme` is released under the [MIT License](./LICENSE)

## Python

- Download Python: [Python](https://www.python.org/downloads/)

### Python3
Required Python Dependencies:
```shell
pip3 install mistletoe
pip3 install colorama
```

### Python
Required Python Dependencies:
```shell
python -m pip install mistletoe
python -m pip install colorama
```

## makeme

- `./makeme install` for installing the project on your computer
- `./makeme uninstall` for uninstalling the project on your computer

### install

- `./makeme install darwin` for installing on your Apple computer
- `./makeme install linux` for installing on your Linux computer
- `./makeme install windows` for installing on your Windows computer

#### Darwin

First you have to put this into your .zshrc
```bash
echo 'export PATH='"$(pwd)"':$PATH' >> ~/.zshrc
source ~/.zshrc
```

#### Linux
Sorry not implemented yet...

#### Windows

```batch
path|find /i "%cd%" >nul || setx path "%PATH%;%cd%"
```

### uninstall

- `./makeme uninstall darwin` for uninstalling on your Apple computer
- `./makeme uninstall linux` for uninstalling on your Linux computer
- `./makeme uninstall windows` for uninstalling on your Windows computer

#### Darwin

```shell
sed -i '' 's#export PATH='"$(pwd)"':$PATH##g' ~/.zshrc
source ~/.zshrc
```

#### Linux
Sorry not implemented yet...

#### Windows
Sorry not implemented yet...
