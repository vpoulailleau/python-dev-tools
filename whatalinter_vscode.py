import subprocess
import sys

# hack for vs code!!!!

new_args = ["whatalinter"]
for arg in sys.argv[1:]:
    if "--format" in arg:
        new_args.append("--format")
        new_args.append('"{}"'.format(arg.split("=")[-1]))
    else:
        new_args.append(arg)
out = subprocess.run(" ".join(new_args), capture_output=True, shell=True)
print(out.stdout.decode("utf-8"))
print(out.stderr.decode("utf-8"), file=sys.stderr)
