import sys
import pathlib

print(sys.path)
sys.path.insert(0, str(pathlib.Path(__file__).parent))
print(sys.path)

from api.online.session import authorisation_challenge

if __name__ == '__main__':
    status_code, response = authorisation_challenge()
    print(status_code, response)