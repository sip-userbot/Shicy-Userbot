#==============×==============#
#      Created by: Nande
#=========× Nande ×=========#

FROM nandeuserbot/nandebot:nande
RUN git clone -b Shicy-Userbot https://github.com/sip-userbot/Shicy-Userbot /home/shicyuserbot/ \
    && chmod 777 /home/shicyuserbot \
    && mkdir /home/shicyuserbot/bin/

COPY ./sample_config.env ./config.env* /home/shicyuserbot/

WORKDIR /home/shicyuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
