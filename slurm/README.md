# Slurm Job Scheduler


## ファイル

### estimate_pi.py

モンテカルロ法を使って円周率の近似値を計算するPythonプログラム


### slurm_estimate_pi.sh

estimate_pi.pyをWrapするSlurmスクリプト。実態はシェルスクリプト。

### batch_jobs.sh

slurm_estimate_pi.sh を ジョブとして、キューに多数スケジュールするシェルスクリプト

### stat.py

カレントディレクトリ上の 出力結果ファイル *.out ファイルを読み、平均を計算する。

## slurmコマンド

### sinfo: 計算ノードの状態確認

### sbatch: ジョブをキューへ追加

### squeue: ジョブキューの確認
