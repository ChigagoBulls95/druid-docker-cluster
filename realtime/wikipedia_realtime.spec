[
  {
    "dataSchema": {
      "dataSource": "wikipedia",
      "parser": {
        "type": "string",
        "parseSpec": {
          "format": "json",
          "timestampSpec": {
            "column": "timestamp",
            "format": "auto"
          },
          "dimensionsSpec": {
            "dimensions": [
              "page",
              "language",
              "user",
              "unpatrolled",
              "newPage",
              "robot",
              "anonymous",
              "namespace",
              "continent",
              "country",
              "region",
              "city"
            ],
            "dimensionExclusions": [],
            "spatialDimensions": []
          }
        }
      },
      "metricsSpec": [
        {
          "type": "count",
          "name": "count"
        },
        {
          "type": "doubleSum",
          "name": "added",
          "fieldName": "added"
        },
        {
          "type": "doubleSum",
          "name": "deleted",
          "fieldName": "deleted"
        },
        {
          "type": "doubleSum",
          "name": "delta",
          "fieldName": "delta"
        }
      ],
      "granularitySpec": {
        "type": "uniform",
        "segmentGranularity": "DAY",
        "queryGranularity": "NONE"
      }
    },
    "ioConfig": {
      "type": "realtime",
      "firehose": {
        "type": "kafka-0.8",
        "consumerProps": {
          "zookeeper.connect": "$ZOOKEEPER_PORT_2181_TCP_ADDR:2181/kafka",
          "zookeeper.connection.timeout.ms": "15000",
          "zookeeper.session.timeout.ms": "15000",
          "zookeeper.sync.time.ms": "5000",
          "group.id": "druid-wikipedia-realtime",
          "fetch.message.max.bytes": "1048586",
          "auto.offset.reset": "largest",
          "auto.commit.enable": "false"
        },
        "feed": "wikipedia"
      },
      "plumber": {
        "type": "realtime"
      }
    },
    "tuningConfig": {
      "type": "realtime",
      "maxRowsInMemory": 500000,
      "intermediatePersistPeriod": "PT10m",
      "windowPeriod": "PT10m",
      "basePersistDirectory": "/tmp/realtime/basePersist",
      "rejectionPolicy": {
        "type": "serverTime"
      }
    }
  }
]