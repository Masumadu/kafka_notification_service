#!/bash/bash

# terminate script if any command returns an error exit code
set -o errexit

# if any pipe command fails, exits
# End the script immediately if any command or pipe exits with a non-zero status.
set -o pipefail

# terminate script if theres an unset variable being used
set -o nounset

function check_postgres_availability {
  python << END
  import sys

  import psycopg2
import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['DEV_DB_HOST'])
print("this is the url", url)
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

try:
    psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)

END
}

until check_postgres_availability; do
  >&2 echo "Waiting for PostgreSQL to become available..." # write to stderr
  sleep 1
done

>&2 echo 'PostgreSQL is available' # write to stderr

exec "$@" # run command passed