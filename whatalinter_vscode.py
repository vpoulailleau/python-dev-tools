"""
Wrapper for whatalinter inside Visual Studio Code.

VS Code wants to import ``whatalinter``, not to execute it.
When ``whatalinter_vscode`` is imported, ``whatalinter`` is executed.
"""
import subprocess  # noqa: S404
import sys

new_args = ["whatalinter"]
for arg in sys.argv[1:]:
    if "--format" in arg:
        new_args.append("--format")
        new_args.append('"{0}"'.format(arg.split("=")[-1]))
    else:
        new_args.append(arg)
out = subprocess.run(" ".join(new_args), capture_output=True, shell=True)  # noqa: S602
print(out.stdout.decode("utf-8"))
print(out.stderr.decode("utf-8"), file=sys.stderr)
