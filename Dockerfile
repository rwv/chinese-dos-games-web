FROM whatwewant/python:v3.10-1

RUN apk --no-cache add git  \
        && pip3 install --upgrade pip  \
        && pip3 install gunicorn flask

RUN zmicro update -a

WORKDIR /app

# Download Games Tool
# RUN GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no" git clone https://github.com/rwv/chinese-dos-games.git /app/games-tools
# Download Games Data (10G)
# RUN python3 /app/games-tools/download_data.py

COPY . .

# Move Games Tools + Data to static
# RUN rm -rf /app/static/games && mv /app/games-tools /app/static/games

EXPOSE 5000

COPY ./entrypoint.sh /entrypoint.sh

CMD /entrypoint.sh
