#!/bin/bash

wait_for_pool() {
  local host="$1"
  local port="$2"
  local timeout=10
  local start_time="$(date +%s)"

  local nc_command="nc"
  type $nc_command > /dev/null 2>&1 || nc_command="ncat"

  while ! $nc_command -z "$host" "$port"; do
      sleep 1
      local current_time="$(date +%s)"
      local elapsed_time=$((current_time - start_time))
      echo "trying to connect to pg via $host:$port"

      if [ "$elapsed_time" -ge "$timeout" ]; then
          echo "timed out waiting for $host:$port"
          exit 1
      fi
  done
}

wait_for_pool "postgres" "$POSTGRES_PORT"

python manage.py runserver "0.0.0.0:$DJANGO_PORT"