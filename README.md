# dotfiles

## Cloning
```bash
cd ~
git clone --bare https://github.com/jbuerklin/dotfiles.git .git
git config --unset core.bare
git config --local status.showUntrackedFiles no
git checkout
```

## To set up imgCat
```bash
cd ~
bin/imgCat/setup.sh
```
