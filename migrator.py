import argparse
from arnold import main
from arnoldexample import db

parser = argparse.ArgumentParser(description='down up')
parser.add_argument('direction', help='the direction to go')

args = parser.parse_args()
main(
    direction=args.direction,
    database=db,
    directory="arnoldexample/migrations",
    migration_module="arnoldexample.migrations"
)
