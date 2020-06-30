## How to run
`conda activate shipyard-monorepo`
`cd /to/this/folder`
`..\shipyard pool add`
`..\shipyard jobs add --tail stdout.txt`
`..\shipyard jobs del -y --wait`
`..\shipyard pool del -y`


## Note
- use `--tail` is to live-stram the stdout.txt to console
- use `PYTHONUNBUFFERED: 1` is to not buffer puthon log out
- after job run you can use `data` command to get stream data for specific job, task and file
    `..\shipyard data files stream --filespec job6,task-00000,stdout.txt`
- you can use `--disk` to stream data into disk
    `..\shipyard data files stream --disk --filespec job6,task-00000,stdout.txt`

