
# MAKEME Project

`makeme` is a build tool that automates the installation and setup process based on the instructions provided in the README file. It is designed to simplify the build workflow by executing commands.

## License
`makeme` is released under the [MIT License](./LICENSE)

## Python

Required Python Dependencies:
```shell
pip3 install mistletoe
pip3 install colorama
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
Sorry not implemented yet...

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
