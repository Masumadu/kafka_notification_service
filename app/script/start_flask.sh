#!/bin/bash

# terminate script if any command fails
set -o errexit

# terminate script if any pipe command fails
set -o pipefail

# terminate script if any variabel being used not set
set -o nounset

flask run