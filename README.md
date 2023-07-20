# ::set-output migrator

## Abstract

Change all workflows using `::set-output` to write to $GITHUB_OUTPUT environment files.

## Why?

I'm lazy. Microsoft will deprecate it's usage in an undefined time as stated [here](https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/),

## Docs 

### Parameters

| short | long     | required | default | help                                     |
|-------|----------|----------|---------|------------------------------------------|
| -p    | --path   | True     | None    | File to change                           |
| -d    | --dry    | False    | False   | Don't apply changes                      |
| -b    | --backup | False    | False   | Create a .bak with the original contents |

### How to use it

An example execution could look like this: 

```sh
python setOutputDeprecation.py -p ./action.yml
```

You can also create some sort of discovery script that searches for all `.yml` or `.yaml` files under `.github`. I've done a dubious attempt under [`migrate-set-output.sh`](./migrate-set-output.sh).

### Develop

I'm using [Pipenv](https://pypi.org/project/pipenv) to create a virtual environment. Use the following command under the root of the project to create the `.venv` file,

```sh
python -m pipenv shell
```

And as such, use [Pipenv](https://pypi.org/project/pipenv) to add dependencies and whatnot.
