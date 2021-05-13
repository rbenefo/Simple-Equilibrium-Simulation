import random
import matplotlib.pyplot as plt
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--bottle_1_num', type=int, 
		default='10',
		help='Number of particles in Bottle 1. Default: 10')

	parser.add_argument('--bottle_2_num', type=int, 
		default=10000,
		help='Number of particles in Bottle 2. Default: 10,000')

	parser.add_argument('--transition_likelihood', type=float, 
		default=0.125,
		help='Likelihood of an element of population 1 making a transition to population 2, or vice versa. Default: 0.125')

	parser.add_argument('--iterations', type=int, 
		default=100,
		help='Number of simulation iterations. Default: 100')

	args = parser.parse_args()
	return args



def main(r1, r2, threshold, iterations):
	r1_list = []
	r2_list = []
	for i in range(iterations):
		r1_list.append(r1)
		r2_list.append(r2)
		to_move_R1 = 0
		to_move_R2 = 0
		for i in range(r1):
			roll_1 = random.random()
			if roll_1 < threshold:
				to_move_R1 += 1
		for i in range(r2):
			roll_2 = random.random()
			if roll_2 < threshold:
				to_move_R2 += 1
		r2 += to_move_R1
		r1 -= to_move_R1
		r1 += to_move_R2
		r2 -= to_move_R2

	fig, ax = plt.subplots()

	ax.plot(r1_list, label="Bottle 1")
	ax.plot(r2_list, label="Bottle 2")
	ax.set_xlabel("Simulation Iterations")
	ax.set_ylabel("Number of Particles")
	ax.legend()
	fig.tight_layout()
	plt.show()

if __name__ == "__main__":
	global args
	args = parse_args()
	main(args.bottle_1_num, args.bottle_2_num, args.transition_likelihood, args.iterations)


