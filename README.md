# sat_tw

Download SAT instances (see e.g., https://baldur.iti.kit.edu/sat-competition-2017/index.php?cat=benchmarks)

Install htd (see, https://github.com/mabseher/htd)


Usage

```bash
./gen_primal.py -f ~/benchmarks/sat/NoLimits/mp1-21.0.cnf.bz2 | htd_main --output width
```
