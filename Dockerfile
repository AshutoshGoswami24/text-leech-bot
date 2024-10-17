# Use a lightweight base image
FROM alpine:latest

<<<<<<< HEAD
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD python3 modules/main.py
=======
# Install echo command with color support
RUN apk add --no-cache bash

# Set the command to be executed when the container starts
CMD echo -e "\033[1;33m🚫 This version of the repo \033[1;34mv1.1\033[0m \033[1;33mdoes not support Docker.\033[0m\n\n🌐 Check it out here: \033[1;32mhttps://github.com/AshutoshGoswami24/text-leech-bot/tree/v1.1\033[0m\n\n\033[1;31mStay tuned for updates!\033[0m"
>>>>>>> origin/main
