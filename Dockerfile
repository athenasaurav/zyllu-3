FROM rasa/rasa-sdk:1.10.0
# Use subdirectory as working directory
WORKDIR /app
# Copy any additional custom requirements, if necessary (uncomment next line)
COPY actions/requirements-actions.txt ./
# Change back to root user to install dependencies
USER root
# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip install rasa[spacy]
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en
RUN pip install -r requirements-actions.txt
# Copy actions folder to working directory
COPY ./actions /app/actions
COPY creds.json /app
# By best practices, don't run the code with root user
USER 1001
EXPOSE 5005
CMD ["start", "--actions", "actions.actions"]