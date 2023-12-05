# 2023

## Setup

```sh
conda activate aoc
pip install advent-cli
```

```sh
# Set session cookie
(cd $CONDA_PREFIX && code ./etc/conda/activate.d/env_vars.sh)

advent --help
# usage: advent [-h] [-v] {get,stats,test,submit,countdown} ...

# options:
#   -h, --help            show this help message and exit
#   -v, --version         show program's version number and exit

# subcommands:
#   use advent {subcommand} --help for arguments

#   {get,stats,test,submit,countdown}
#     get                 download prompt and input, generate solution template
#     stats               show personal stats or private leaderboards
#     test                run solution and output answers without submitting
#     submit              run solution and submit answers
#     countdown           display countdown to puzzle unlock
```

## Workflow

<https://github.com/fergusch/advent-cli>


```sh
# Get puzzle & input data
advent get YYYY/DD

# <activate brain here>

# Run code against example_input.txt
advent test YYYY/DD -e
# Run code against input.txt
advent test YYYY/DD

# Submit answers
advent submit YYYY/DD
```

```sh
# Check leaderboard
advent stats --private
```
