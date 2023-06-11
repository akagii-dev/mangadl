import argparse
from lib import Download
parser = argparse.ArgumentParser(description="tool for downloading comics")
parser.add_argument("-e", "--episode", help="input a episode URL")

args = parser.parse_args()

download = Download(args.episode)
download.mkdirs()
download.save_pages()