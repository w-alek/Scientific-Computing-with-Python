from environs import Env

env = Env()
env.read_env()

DATA_PATH = env.str("DATA")

RESULTS_PATH = env.str("RESULTS")

WIDTH = env.int("WIDTH")

HEIGHT = env.int("HEIGHT")

PREPROCESS_FUNC = env.str("PREPROCESS")

EXTENSION = env.str("EXTENSION")

EPSILON = env.float("EPSILON")