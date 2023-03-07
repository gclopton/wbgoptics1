import os

current_dir = os.getcwd()
print(current_dir)

system_path = os.path.abspath(os.path.join(os.getcwd(), "../../../"))
chg_path = os.path.abspath(os.path.join(os.getcwd(), "../../"))
functional_path = os.path.abspath(os.path.join(os.getcwd(), "../"))

system = os.path.basename(system_path)
print(system)
chg = os.path.basename(chg_path)
print(chg)
functional = os.path.basename(functional_path)
print(functional)


