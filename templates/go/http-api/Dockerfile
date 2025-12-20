FROM golang:1.22-alpine AS build

WORKDIR /src

COPY go.mod ./
COPY app ./app

RUN go build -o /out/server ./app

FROM alpine:3.20

RUN adduser -D -u 10001 app
USER app

COPY --from=build /out/server /server

EXPOSE 8080

CMD ["/server"]
