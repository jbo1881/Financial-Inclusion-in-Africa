{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Importing libraries"
      ],
      "metadata": {
        "id": "KJHrUomOTrKw"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "mD7EcYx7TLXI"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Loading datasets\n",
        "\n"
      ],
      "metadata": {
        "id": "0muWbanNU0Ib"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train = pd.read_csv('/AFRICA/Train.csv')\n",
        "test = pd.read_csv('/AFRICA/Test.csv')"
      ],
      "metadata": {
        "id": "OJh0v4vJUXdu"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Print first 5 rows of the train dataset"
      ],
      "metadata": {
        "id": "C30DGhZOVFUN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 330
        },
        "id": "tHvXtU08VMy1",
        "outputId": "4cf5447c-d375-4e1e-a75c-a9f96361af2d"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  country  year    uniqueid bank_account location_type cellphone_access  \\\n",
              "0   Kenya  2018  uniqueid_1          Yes         Rural              Yes   \n",
              "1   Kenya  2018  uniqueid_2           No         Rural               No   \n",
              "2   Kenya  2018  uniqueid_3          Yes         Urban              Yes   \n",
              "3   Kenya  2018  uniqueid_4           No         Rural              Yes   \n",
              "4   Kenya  2018  uniqueid_5           No         Urban               No   \n",
              "\n",
              "   household_size  age_of_respondent gender_of_respondent  \\\n",
              "0               3                 24               Female   \n",
              "1               5                 70               Female   \n",
              "2               5                 26                 Male   \n",
              "3               5                 34               Female   \n",
              "4               8                 26                 Male   \n",
              "\n",
              "  relationship_with_head           marital_status  \\\n",
              "0                 Spouse  Married/Living together   \n",
              "1      Head of Household                  Widowed   \n",
              "2         Other relative     Single/Never Married   \n",
              "3      Head of Household  Married/Living together   \n",
              "4                  Child     Single/Never Married   \n",
              "\n",
              "                   education_level                   job_type  \n",
              "0              Secondary education              Self employed  \n",
              "1              No formal education       Government Dependent  \n",
              "2  Vocational/Specialised training              Self employed  \n",
              "3                Primary education  Formally employed Private  \n",
              "4                Primary education        Informally employed  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-8cc3390b-9d96-43c6-aa67-51913b092203\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>country</th>\n",
              "      <th>year</th>\n",
              "      <th>uniqueid</th>\n",
              "      <th>bank_account</th>\n",
              "      <th>location_type</th>\n",
              "      <th>cellphone_access</th>\n",
              "      <th>household_size</th>\n",
              "      <th>age_of_respondent</th>\n",
              "      <th>gender_of_respondent</th>\n",
              "      <th>relationship_with_head</th>\n",
              "      <th>marital_status</th>\n",
              "      <th>education_level</th>\n",
              "      <th>job_type</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Kenya</td>\n",
              "      <td>2018</td>\n",
              "      <td>uniqueid_1</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Rural</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3</td>\n",
              "      <td>24</td>\n",
              "      <td>Female</td>\n",
              "      <td>Spouse</td>\n",
              "      <td>Married/Living together</td>\n",
              "      <td>Secondary education</td>\n",
              "      <td>Self employed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Kenya</td>\n",
              "      <td>2018</td>\n",
              "      <td>uniqueid_2</td>\n",
              "      <td>No</td>\n",
              "      <td>Rural</td>\n",
              "      <td>No</td>\n",
              "      <td>5</td>\n",
              "      <td>70</td>\n",
              "      <td>Female</td>\n",
              "      <td>Head of Household</td>\n",
              "      <td>Widowed</td>\n",
              "      <td>No formal education</td>\n",
              "      <td>Government Dependent</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Kenya</td>\n",
              "      <td>2018</td>\n",
              "      <td>uniqueid_3</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Urban</td>\n",
              "      <td>Yes</td>\n",
              "      <td>5</td>\n",
              "      <td>26</td>\n",
              "      <td>Male</td>\n",
              "      <td>Other relative</td>\n",
              "      <td>Single/Never Married</td>\n",
              "      <td>Vocational/Specialised training</td>\n",
              "      <td>Self employed</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Kenya</td>\n",
              "      <td>2018</td>\n",
              "      <td>uniqueid_4</td>\n",
              "      <td>No</td>\n",
              "      <td>Rural</td>\n",
              "      <td>Yes</td>\n",
              "      <td>5</td>\n",
              "      <td>34</td>\n",
              "      <td>Female</td>\n",
              "      <td>Head of Household</td>\n",
              "      <td>Married/Living together</td>\n",
              "      <td>Primary education</td>\n",
              "      <td>Formally employed Private</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Kenya</td>\n",
              "      <td>2018</td>\n",
              "      <td>uniqueid_5</td>\n",
              "      <td>No</td>\n",
              "      <td>Urban</td>\n",
              "      <td>No</td>\n",
              "      <td>8</td>\n",
              "      <td>26</td>\n",
              "      <td>Male</td>\n",
              "      <td>Child</td>\n",
              "      <td>Single/Never Married</td>\n",
              "      <td>Primary education</td>\n",
              "      <td>Informally employed</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8cc3390b-9d96-43c6-aa67-51913b092203')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-8cc3390b-9d96-43c6-aa67-51913b092203 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-8cc3390b-9d96-43c6-aa67-51913b092203');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-e8829156-a14c-4fa5-98ff-037d0b21a939\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-e8829156-a14c-4fa5-98ff-037d0b21a939')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-e8829156-a14c-4fa5-98ff-037d0b21a939 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "train",
              "summary": "{\n  \"name\": \"train\",\n  \"rows\": 23524,\n  \"fields\": [\n    {\n      \"column\": \"country\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Rwanda\",\n          \"Uganda\",\n          \"Kenya\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 2016,\n        \"max\": 2018,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          2018,\n          2016,\n          2017\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"uniqueid\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 8735,\n        \"samples\": [\n          \"uniqueid_3028\",\n          \"uniqueid_1722\",\n          \"uniqueid_1264\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"bank_account\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"location_type\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Urban\",\n          \"Rural\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cellphone_access\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"household_size\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2,\n        \"min\": 1,\n        \"max\": 21,\n        \"num_unique_values\": 20,\n        \"samples\": [\n          3,\n          18\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"age_of_respondent\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 16,\n        \"min\": 16,\n        \"max\": 100,\n        \"num_unique_values\": 85,\n        \"samples\": [\n          92,\n          24\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"gender_of_respondent\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Male\",\n          \"Female\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"relationship_with_head\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Spouse\",\n          \"Head of Household\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"marital_status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Widowed\",\n          \"Dont know\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"education_level\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Secondary education\",\n          \"No formal education\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"job_type\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 10,\n        \"samples\": [\n          \"Dont Know/Refuse to answer\",\n          \"Government Dependent\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Number of rows and columns of train dataset"
      ],
      "metadata": {
        "id": "YGzOSsOfWFCD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "65MlBZxAWIOG",
        "outputId": "63872f9f-d27a-4f87-9d3d-5a7d006e481c"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(23524, 13)"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Info about the train dataset"
      ],
      "metadata": {
        "id": "fpzzaSCRWUCl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "S1yuQn41WWP9",
        "outputId": "a7173096-5da1-4470-adc8-f4d215a0dce8"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 23524 entries, 0 to 23523\n",
            "Data columns (total 13 columns):\n",
            " #   Column                  Non-Null Count  Dtype \n",
            "---  ------                  --------------  ----- \n",
            " 0   country                 23524 non-null  object\n",
            " 1   year                    23524 non-null  int64 \n",
            " 2   uniqueid                23524 non-null  object\n",
            " 3   bank_account            23524 non-null  object\n",
            " 4   location_type           23524 non-null  object\n",
            " 5   cellphone_access        23524 non-null  object\n",
            " 6   household_size          23524 non-null  int64 \n",
            " 7   age_of_respondent       23524 non-null  int64 \n",
            " 8   gender_of_respondent    23524 non-null  object\n",
            " 9   relationship_with_head  23524 non-null  object\n",
            " 10  marital_status          23524 non-null  object\n",
            " 11  education_level         23524 non-null  object\n",
            " 12  job_type                23524 non-null  object\n",
            "dtypes: int64(3), object(10)\n",
            "memory usage: 2.3+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Missing values by column"
      ],
      "metadata": {
        "id": "C-GofrK4W7eI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train.isna().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "TcCWI_ppW9u8",
        "outputId": "18a77f56-1a34-406e-cec6-13b7d9762e9e"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "country                   0\n",
              "year                      0\n",
              "uniqueid                  0\n",
              "bank_account              0\n",
              "location_type             0\n",
              "cellphone_access          0\n",
              "household_size            0\n",
              "age_of_respondent         0\n",
              "gender_of_respondent      0\n",
              "relationship_with_head    0\n",
              "marital_status            0\n",
              "education_level           0\n",
              "job_type                  0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Data Analysis"
      ],
      "metadata": {
        "id": "dvS2mkQ5XGN_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Statistical analysis"
      ],
      "metadata": {
        "id": "6wyHGX2tX2Q6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "4cnRbsUoXpox",
        "outputId": "963b3f9b-1f6a-4244-cd4e-508bd7e504d6"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "               year  household_size  age_of_respondent\n",
              "count  23524.000000    23524.000000       23524.000000\n",
              "mean    2016.975939        3.797483          38.805220\n",
              "std        0.847371        2.227613          16.520569\n",
              "min     2016.000000        1.000000          16.000000\n",
              "25%     2016.000000        2.000000          26.000000\n",
              "50%     2017.000000        3.000000          35.000000\n",
              "75%     2018.000000        5.000000          49.000000\n",
              "max     2018.000000       21.000000         100.000000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-8656fdf2-79c5-4026-880f-c58f29f70e11\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>year</th>\n",
              "      <th>household_size</th>\n",
              "      <th>age_of_respondent</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>23524.000000</td>\n",
              "      <td>23524.000000</td>\n",
              "      <td>23524.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2016.975939</td>\n",
              "      <td>3.797483</td>\n",
              "      <td>38.805220</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.847371</td>\n",
              "      <td>2.227613</td>\n",
              "      <td>16.520569</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>2016.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>16.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2016.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>26.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>2017.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>35.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>2018.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>49.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2018.000000</td>\n",
              "      <td>21.000000</td>\n",
              "      <td>100.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8656fdf2-79c5-4026-880f-c58f29f70e11')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-8656fdf2-79c5-4026-880f-c58f29f70e11 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-8656fdf2-79c5-4026-880f-c58f29f70e11');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-2c38658f-b65b-4803-b0dc-b7e8b4851ced\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-2c38658f-b65b-4803-b0dc-b7e8b4851ced')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-2c38658f-b65b-4803-b0dc-b7e8b4851ced button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"train\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7737.934389032701,\n        \"min\": 0.8473705735442522,\n        \"max\": 23524.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          23524.0,\n          2016.9759394660773,\n          2018.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"household_size\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 8315.07191837213,\n        \"min\": 1.0,\n        \"max\": 23524.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          3.797483421186873,\n          3.0,\n          23524.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"age_of_respondent\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 8302.82413901166,\n        \"min\": 16.0,\n        \"max\": 23524.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          38.80522020064615,\n          35.0,\n          23524.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "People with and without bank account"
      ],
      "metadata": {
        "id": "BtGrfko6YoF_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train['bank_account'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "8lZLVqF0YsFB",
        "outputId": "aa26f679-11dd-465d-c286-fa18f2cec86b"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "bank_account\n",
              "No     20212\n",
              "Yes     3312\n",
              "Name: count, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Data Visualization"
      ],
      "metadata": {
        "id": "FrLJ3fbcZU4v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.set()"
      ],
      "metadata": {
        "id": "DsbDmEltZXB5"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Count plot of bank accounts"
      ],
      "metadata": {
        "id": "kujTB6sgZl0z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(x='bank_account', data=train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 476
        },
        "id": "qRi1r6ajZp7u",
        "outputId": "87034f82-0f4b-4083-9a0d-f0e9ae652d57"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='bank_account', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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/vKXeuaZZ7R//3517drV69hbb72lU6dO6a9//asiIyMlST179lTfvn21cuVKTZ482Rctw0dYwQIMMGbMGEnSE088oYCAAH344YeKi4tTaGioKioqVFFRIbPZrJ49e+qzzz6TJEVHRysgIEATJ07U+++/r6KiIl+eAoBaGDBggKKioq66irV7927deeednnAlSc2aNdO9996rTz/99IdsEw0AK1iAARo1auT19dy5c9q7d6/uueeeGrXt27eXJEVERGjp0qVatmyZnn76aZnNZiUmJmrGjBlq06bND9c8gFozmUwaN26cnn32WX3++edex1wul370ox/VeE7z5s119OjRH6pFNBAELKAehIaGqk+fPho/fnyNYxaLxfPvSUlJSkpKUnFxsfLy8jR79mxNmTJFK1eu/CHbBXAdBg0apMWLF+ull17y+p+h0NBQFRQU1Kj/5ptvFBoa+kO2iAaAS4RAPbj33nv15ZdfKjIyUl26dPH6Jzo6ukZ9kyZNlJKSosGDB+vLL7/0QccAastsNmvcuHHatm2b128I9ujRQ0eOHJHD4fCMOZ1OffTRR+rRo4cvWoUPsYIF1IPHH39cGzdu1KhRo/Too4+qTZs2Kiws1L59+9SqVSs9/vjjev3117V371716dNHLVq00IkTJ/SXv/xFCQkJvm4fwPcYOnSoXnzxRX388cdq27atJGn48OH605/+pLFjxyorK0tBQUH64x//qMDAQD322GM+7hg/NAIWUA/CwsL0xhtvaMGCBZo7d67Onz+v5s2bq1u3bhowYICky5vct2/frtmzZ+v8+fNq0aKFBg8efNXLigAaloCAAI0ZM0bTpk3zjDVp0kSrVq3SnDlzNH36dFVVVal79+5avXq1Wrdu7cNu4Qsmt9vt9nUTAAAANxP2YAEAABiMgAUAAGAwAhYAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAfCJxYsXKzo6WoWFhT/o67711luKjo7WZ5999oO+LoBbCwELAPC9Nm7cqD/96U++bgPwGwQsAMD3euedd/Tqq6/6ug3AbxCwAAAADEbAAuBT586d0/jx49W9e3fFxcXpv/7rv3Tp0iXP8Q0bNujRRx9VfHy8OnfurJSUFL322ms15unXr5/Gjh2r3bt366GHHlKXLl2UnJysP//5z9/bg9Pp1EMPPaSkpCQ5HI5a9V1WVqaFCxdq+PDh6tGjh2JiYvTII4/o73//e43aqqoqrVy5UkOHDlWXLl3Uu3dvZWRk1NgH9vbbb+uhhx5St27d1LNnT40cOVI7d+70qlmzZo0GDx6szp07KzExUbNmzZLL5arxvZg8eXKNPtLS0pSWluZ5/PHHHys6Olq5ubn64x//qKSkJHXp0kWPPfaYjh075vW8v/3tbzp58qSio6MVHR2tfv361er7BNyqAn3dAIBbW1ZWltq2basJEyZo7969WrVqlVwul37/+99LktauXas777xT/fr1U2BgoLZv365Zs2bJ7XZr5MiRXnMdO3ZM48eP10MPPaSf/exn2rBhgyZPnqx77rlHd95551Vfv7CwUOnp6XI6nVq9erXat29fq76Li4u1fv16DRkyRA8//LAuXLigN998U08++aTWr1+vTp06eWr/z//5P3rrrbeUlJSkhx56SJWVldq9e7f27dunLl26SJKWLFmixYsXKzY2VpmZmWrUqJH27dunv//970pMTJR0+RcDlixZonvvvVepqakqKCjQ2rVr9dlnn2nt2rVq1KjRdX//JSknJ0cmk0np6ekqLi7WihUrNHHiRK1fv16SNG7cOBUVFenMmTOaMmWKJKlx48Z1ei3gluEGAB9YtGiROyoqyj1u3Div8ZkzZ7qjoqLchw4dcrvdbndpaWmN56anp7uTk5O9xvr27euOiopy/+Mf//CMffPNN+7OnTu758yZ4xnbsGGDOyoqyr1//3732bNn3YMHD3YnJye7T5w4cV39V1RUuC9duuQ15nQ63ffee697ypQpnrFdu3a5o6Ki3L/73e9qzFFVVeV2u93ur776yn3XXXe5n3rqKXdlZeVVa7755hv3Pffc405PT/eqWb16tTsqKsr95ptven0vJk2aVOP1Ro0a5R41apTn8d///nd3VFSUe9CgQV7nsnLlSndUVJT78OHDnrExY8a4+/bt+93fFAAeXCIE4FPfXoUaNWqUJCkvL0+SdNttt3mOFRUVqbCwUL169dLx48dVVFTk9dw77rhDP/nJTzyPw8PDFRERoePHj9d43X//+98aNWqUysvLtWbNGrVt2/a6+g4ICJDFYpF0+RLg+fPnVVFRoc6dO+vgwYOeui1btshkMunpp5+uMYfJZJIkvffee6qqqtJTTz0ls9l81ZqPPvpI5eXlevTRR71qHn74YTVp0kQ7duy4rv6vNHz4cM+5SPJ8D6/2fQNQO1wiBOBTHTp08Hrcvn17mc1mnThxQpL06aefavHixdq7d69KS0u9aouKitS0aVPP49atW9eYPzQ0VE6ns8b4r3/9awUGBio3N1ctWrSoU+//8z//o5dfflkFBQUqLy/3jN9+++2ef//Xv/6lli1bqlmzZtec51//+pfMZrMiIyOvWXPq1ClJks1m8xq3WCxq166dTp48WadzkKQ2bdp4PbZarZJUY28XgNpjBQtAg1K9YiNdDh6PP/64zp07p8mTJ2v58uV65ZVX9Pjjj0u6vHJ0pYCAgFq/zsCBA+Vyuep864G3335bkydPVvv27fVf//VfWrFihV555RX17t1bbre7TnPWt8rKyquOf3vVrFpDPQ/AH7CCBcCnjh07pnbt2nk9rqqq0u233673339fZWVl+uMf/+i1yvLxxx/f8OuOGjVK7du316JFi9S0aVONGTPmup7/7rvvql27dlqyZIlXKFy0aJFXXfv27bVz506dP3/+mqtY7du3V1VVlb788kuvzfFXqj5/h8Ph9f0qKyvTiRMndO+993rGQkNDr7r6dOrUKa/nXo8rzxHA92MFC4BPrVmzxuvx6tWrJUlJSUmeFakrV1KKioq0YcMGQ177qaeeUnp6ul544YWr3vrhu1ytt3379mnv3r1edQMHDpTb7daSJUtqzFH93P79+8tsNuvFF1+ssSpXXXPvvfeqUaNGWrVqlddrvvnmmyoqKtJ9993nGWvXrp327dunsrIyz9j27dt1+vTp6zrHKwUHB9fY8wbg2ljBAuBTJ06c0Lhx49SnTx/t3btXf/nLXzRkyBDdddddslgsatSokcaNG6df/OIXunDhgtavX6/mzZvr66+/NuT1J02apOLiYv32t79V48aNNWzYsFo97/7779eWLVv01FNP6f7779eJEyf0+uuv64477lBJSYmnrnfv3ho2bJhWrVqlY8eOqU+fPqqqqtKnn36quLg4jRo1Sh06dNC4ceP00ksv6ZFHHtHAgQNlsVj02WefqWXLlpowYYLCw8M1duxYLVmyRE8++aT69eungoICvfbaa+rSpYt++tOfel7z4Ycf1rvvvqsnn3xSgwYN0r/+9S9t3Lix1reguJp77rlHubm5mj17trp06aKQkBDuhQV8BwIWAJ9asGCBFi5cqBdeeEGBgYEaNWqUfvOb30i6vKF70aJFWrBggZ5//nn96Ec/UmpqqsLDwzV16lTDepg1a5ZKSko0depUNW7cWP379//e5wwfPlz/+7//qzfeeEM7d+7UHXfcoT/84Q/avHmzPvnkE6/a2bNnKzo6Wm+++aZ+//vfq2nTpurcubNiY2M9NePHj9ftt9+u1atXa/78+QoODlZ0dLRX4HvmmWcUHh6u1atXa/bs2QoNDdXPf/5zPfvss173wOrTp48mT56sV155Rc8995w6d+6spUuX6vnnn6/z9+iRRx7RoUOH9NZbb+lPf/qT2rZtS8ACvoPJzS5GAAAAQ7EHCwAAwGBcIgSAK5SVlV31vllXatq0qdcNUAHg2whYAHCF/Px8Pfroo99ZM3v2bA0fPvwH6giAP2IPFgBcwel06vPPP//OmjvuuEMtW7b8gToC4I8IWAAAAAZjkzsAAIDBCFgAAAAGI2ABAAAYjIAFAABgMAIWAACAwQhYAAAABiNgAQAAGOz/A320Uq2DfToVAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "Count plot of gender\n"
      ],
      "metadata": {
        "id": "2A_7LRd5b_1G"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(x='gender_of_respondent', hue='bank_account',data=train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 476
        },
        "id": "1NNJwH26aav1",
        "outputId": "dec8b142-6a94-458b-e794-2276d4e75b71"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='gender_of_respondent', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 11
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Encoding categorical columns"
      ],
      "metadata": {
        "id": "G82UNIf2dWkc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import OneHotEncoder"
      ],
      "metadata": {
        "id": "KcKuXcISeR98"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Drop 'year' column as it's not relevant for prediction\n",
        "train.drop('year', axis=1, inplace=True)\n",
        "test.drop('year', axis=1, inplace=True)\n",
        "\n",
        "# Drop 'uniqueid' from features\n",
        "train.drop('uniqueid', axis=1, inplace=True)\n",
        "test_unique_ids = test['uniqueid']  # Store unique IDs for final output\n",
        "test_countries = test['country']\n",
        "test.drop('uniqueid', axis=1, inplace=True)"
      ],
      "metadata": {
        "id": "F7Nd1BuwdZyN"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Define categorical columns for encoding\n",
        "categorical_columns = ['country', 'location_type', 'cellphone_access',\n",
        "                       'gender_of_respondent', 'relationship_with_head',\n",
        "                       'marital_status', 'education_level', 'job_type']\n",
        "\n",
        "# Iterate through categorical columns and create encoders\n",
        "for column in categorical_columns:\n",
        "    # One-Hot Encoding\n",
        "    one_hot_enc = OneHotEncoder(handle_unknown='ignore')\n",
        "    train_encoded = one_hot_enc.fit_transform(train[[column]])\n",
        "    test_encoded = one_hot_enc.transform(test[[column]])\n",
        "\n",
        "    # Merge the encoded columns back to the dataframe\n",
        "    train_encoded_df = pd.DataFrame(train_encoded.toarray(),\n",
        "              columns=[f\"{column}_{i}\" for i in range(train_encoded.shape[1])],\n",
        "                                    index=train.index)\n",
        "    test_encoded_df = pd.DataFrame(test_encoded.toarray(),\n",
        "            columns=[f\"{column}_{i}\" for i in range(test_encoded.shape[1])],\n",
        "                                   index=test.index)\n",
        "\n",
        "    train = pd.concat([train, train_encoded_df], axis=1)\n",
        "    test = pd.concat([test, test_encoded_df], axis=1)\n",
        "\n",
        "# Drop original categorical columns from train and test data\n",
        "train.drop(categorical_columns, axis=1, inplace=True)\n",
        "test.drop(categorical_columns, axis=1, inplace=True)"
      ],
      "metadata": {
        "id": "t_vyRrWseAAd"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 255
        },
        "id": "a-thxsUIepWI",
        "outputId": "1e42eb2c-e3af-481b-b513-af2092e3bcfd"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  bank_account  household_size  age_of_respondent  country_0  country_1  \\\n",
              "0          Yes               3                 24        1.0        0.0   \n",
              "1           No               5                 70        1.0        0.0   \n",
              "2          Yes               5                 26        1.0        0.0   \n",
              "3           No               5                 34        1.0        0.0   \n",
              "4           No               8                 26        1.0        0.0   \n",
              "\n",
              "   country_2  country_3  location_type_0  location_type_1  cellphone_access_0  \\\n",
              "0        0.0        0.0              1.0              0.0                 0.0   \n",
              "1        0.0        0.0              1.0              0.0                 1.0   \n",
              "2        0.0        0.0              0.0              1.0                 0.0   \n",
              "3        0.0        0.0              1.0              0.0                 0.0   \n",
              "4        0.0        0.0              0.0              1.0                 1.0   \n",
              "\n",
              "   ...  job_type_0  job_type_1  job_type_2  job_type_3  job_type_4  \\\n",
              "0  ...         0.0         0.0         0.0         0.0         0.0   \n",
              "1  ...         0.0         0.0         0.0         0.0         1.0   \n",
              "2  ...         0.0         0.0         0.0         0.0         0.0   \n",
              "3  ...         0.0         0.0         0.0         1.0         0.0   \n",
              "4  ...         0.0         0.0         0.0         0.0         0.0   \n",
              "\n",
              "   job_type_5  job_type_6  job_type_7  job_type_8  job_type_9  \n",
              "0         0.0         0.0         0.0         0.0         1.0  \n",
              "1         0.0         0.0         0.0         0.0         0.0  \n",
              "2         0.0         0.0         0.0         0.0         1.0  \n",
              "3         0.0         0.0         0.0         0.0         0.0  \n",
              "4         1.0         0.0         0.0         0.0         0.0  \n",
              "\n",
              "[5 rows x 40 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b1fdba78-472c-4dce-aee3-f4ea1188778c\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>bank_account</th>\n",
              "      <th>household_size</th>\n",
              "      <th>age_of_respondent</th>\n",
              "      <th>country_0</th>\n",
              "      <th>country_1</th>\n",
              "      <th>country_2</th>\n",
              "      <th>country_3</th>\n",
              "      <th>location_type_0</th>\n",
              "      <th>location_type_1</th>\n",
              "      <th>cellphone_access_0</th>\n",
              "      <th>...</th>\n",
              "      <th>job_type_0</th>\n",
              "      <th>job_type_1</th>\n",
              "      <th>job_type_2</th>\n",
              "      <th>job_type_3</th>\n",
              "      <th>job_type_4</th>\n",
              "      <th>job_type_5</th>\n",
              "      <th>job_type_6</th>\n",
              "      <th>job_type_7</th>\n",
              "      <th>job_type_8</th>\n",
              "      <th>job_type_9</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Yes</td>\n",
              "      <td>3</td>\n",
              "      <td>24</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>...</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>No</td>\n",
              "      <td>5</td>\n",
              "      <td>70</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>...</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Yes</td>\n",
              "      <td>5</td>\n",
              "      <td>26</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>...</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>No</td>\n",
              "      <td>5</td>\n",
              "      <td>34</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>...</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>No</td>\n",
              "      <td>8</td>\n",
              "      <td>26</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>...</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 40 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b1fdba78-472c-4dce-aee3-f4ea1188778c')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-b1fdba78-472c-4dce-aee3-f4ea1188778c button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-b1fdba78-472c-4dce-aee3-f4ea1188778c');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-0717b09b-c768-4d2a-9bc4-b3ce0e09d2b7\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-0717b09b-c768-4d2a-9bc4-b3ce0e09d2b7')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-0717b09b-c768-4d2a-9bc4-b3ce0e09d2b7 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "train"
            }
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Features and Target"
      ],
      "metadata": {
        "id": "30D2UX-TfCHU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_train = train.drop('bank_account', axis=1)\n",
        "y_train = train['bank_account']  # Target variable"
      ],
      "metadata": {
        "id": "xAB_lR1pfGd0"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Model Trainig: Gradient Boosting Classifier"
      ],
      "metadata": {
        "id": "DLlzD_fzhLkL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import cross_val_score\n",
        "from sklearn.ensemble import GradientBoostingClassifier\n",
        "\n",
        "gbr = GradientBoostingClassifier()\n",
        "gbr.fit(X_train, y_train)\n",
        "cross_val_score(gbr, X_train, y_train, cv=3, n_jobs=-1).mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "HhjnnkVPvnD1",
        "outputId": "7096f17d-f964-48a3-8ad4-8c467a67fdd3"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.7226367670908251"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "param_grid = {\n",
        "    'n_estimators': [100, 120, 150, 300],\n",
        "    'learning_rate': [0.0001, 0.001, 0.01, 0.1, 1.0],\n",
        "    'max_depth': [3, 5, 7, 9]\n",
        "}"
      ],
      "metadata": {
        "id": "ehkmjbuUw3Eu"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import GridSearchCV\n",
        "\n",
        "gbr2 = GridSearchCV(gbr, param_grid, cv=3, n_jobs=-1)\n",
        "\n",
        "gbr2.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 117
        },
        "id": "sWLyCOMDxq1u",
        "outputId": "6b3e47da-d3ae-4f10-a402-b1d447233a50"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=3, estimator=GradientBoostingClassifier(), n_jobs=-1,\n",
              "             param_grid={'learning_rate': [0.0001, 0.001, 0.01, 0.1, 1.0],\n",
              "                         'max_depth': [3, 5, 7, 9],\n",
              "                         'n_estimators': [100, 120, 150, 300]})"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>GridSearchCV(cv=3, estimator=GradientBoostingClassifier(), n_jobs=-1,\n",
              "             param_grid={&#x27;learning_rate&#x27;: [0.0001, 0.001, 0.01, 0.1, 1.0],\n",
              "                         &#x27;max_depth&#x27;: [3, 5, 7, 9],\n",
              "                         &#x27;n_estimators&#x27;: [100, 120, 150, 300]})</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" ><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">GridSearchCV</label><div class=\"sk-toggleable__content\"><pre>GridSearchCV(cv=3, estimator=GradientBoostingClassifier(), n_jobs=-1,\n",
              "             param_grid={&#x27;learning_rate&#x27;: [0.0001, 0.001, 0.01, 0.1, 1.0],\n",
              "                         &#x27;max_depth&#x27;: [3, 5, 7, 9],\n",
              "                         &#x27;n_estimators&#x27;: [100, 120, 150, 300]})</pre></div></div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" ><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">estimator: GradientBoostingClassifier</label><div class=\"sk-toggleable__content\"><pre>GradientBoostingClassifier()</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" ><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">GradientBoostingClassifier</label><div class=\"sk-toggleable__content\"><pre>GradientBoostingClassifier()</pre></div></div></div></div></div></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "gbr2.best_params_"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "3hHYZ5YsyaiD",
        "outputId": "6369681a-6832-461a-8543-74766cb24521"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'learning_rate': 0.0001, 'max_depth': 3, 'n_estimators': 100}"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "gbr2.best_score_"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "v7AgZxOp1knw",
        "outputId": "21d3cbbf-acb2-462b-eb3f-08f2a18e9471"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.8592076172432582"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "predictions = gbr2.predict(test)"
      ],
      "metadata": {
        "id": "FNxhUxxcjHcX"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "predictions"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "RXGbIdk2kak6",
        "outputId": "79c541cf-c420-4856-9231-37c7010e37eb"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['No', 'No', 'No', ..., 'No', 'No', 'No'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a dataframe for the predictions with unique IDs\n",
        "predictions_df = pd.DataFrame({'unique_id': test_unique_ids, 'bank_account': predictions})\n",
        "\n",
        "# Map 0s and 1s to 'No' and 'Yes' respectively\n",
        "predictions_df['bank_account'] = predictions_df['bank_account'].map({'No': 0, 'Yes': 1})\n",
        "\n",
        "# Append country name to unique_id column\n",
        "predictions_df['unique_id'] = predictions_df['unique_id'] + ' x ' + test_countries\n",
        "\n",
        "predictions_df['unique_id'].astype('str')\n",
        "\n",
        "# Save the predictions to a CSV file\n",
        "predictions_df.to_csv('PredictionsGBbest.csv', index=False)"
      ],
      "metadata": {
        "id": "eh-f03p6jaDW"
      },
      "execution_count": 25,
      "outputs": []
    }
  ]
}