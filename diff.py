import sys

def load(path):
	ret = {}
	with open(path, "r") as fh:
		for line in fh:
			if "=" not in line:
				continue
			action, key = line.strip().split("=")
			ret[action] = key
	return ret

def diff(p1, p2):
	actions = set(p1.keys()) | set(p2.keys())
	for action in actions:
		if action in p1 and action in p2:
			k1 = p1.get(action)
			k2 = p2.get(action)
			if k1 != k2:
				print(f"{action} = ({k1}) vs ({k2})")

def main():
	diff(load(sys.argv[1]), load(sys.argv[2]))

if __name__ == "__main__":
	main()
