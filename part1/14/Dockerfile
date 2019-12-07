FROM ruby:2.6.0
WORKDIR /app

RUN gem install bundler

RUN apt-get -qq update && apt-get -qq install curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get -qq install nodejs

COPY rails-example-project .
RUN bundle install
RUN rails db:migrate

ENV RAILS_LOG_TO_STDOUT=true
CMD rails s
