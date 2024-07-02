<p><a target="_blank" href="https://app.eraser.io/workspace/o8hc74AnQrLKcf0ufzUD" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# <h1 align="center"><a href="https://github.com/ronknight/alibaba-seller-api">Alibaba Seller API Integration</a></h1>
<h4 align="center">A collection of Python scripts for integrating with Alibaba's Seller API, allowing you to manage orders, logistics, and more.</h4>
<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/alibaba-seller-api/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/alibaba-seller-api/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>
<p align="center">
  <a href="#requirements">Requirements</a> •
  <a href="#setup">Setup</a> •
  <a href="#scripts-overview">Scripts Overview</a> •
  <a href="#usage">Usage</a> •
  <a href="#logging">Logging</a> •
  <a href="#disclaimer">Disclaimer</a> •
  <a href="#diagrams">Diagrams</a>
</p>

---

## Requirements
The project dependencies are listed in the `requirements.txt` file. To install all required packages, run:

```
pip install -r requirements.txt
```
Key dependencies include:

- requests
- python-dotenv
- aiohttp
- alibabacloud-openplatform20191219
- aliyun-python-sdk-core
- and various other packages for data processing and analysis
Additional requirements:

- Python 3.x
- Alibaba Seller API credentials (APP_KEY, APP_SECRET, REDIRECT_URI)
## Setup
1. Clone this repository:git clone https://github.com/ronknight/alibaba-seller-api.git
cd alibaba-seller-api
2. Install required packages:pip install -r requirements.txt
3. Create a `.env`  file in the root directory with your Alibaba API credentials:APP_KEY=your_app_key
APP_SECRET=your_app_secret
REDIRECT_URI=your_redirect_uri
## Scripts Overview
1. **1initiate.py**
    - Initiates the OAuth authorization process
    - Generates the authorization URL
    - Extracts and saves the authorization code and state
2. **2createtoken.py**
    - Creates an access token using the authorization code
    - Updates the .env file with the new session key (access token)
    - Logs API requests and responses
3. **sellerorderlist.py**
    - Retrieves a list of seller orders
    - Uses the alibaba.seller.order.list API method
    - Logs API requests and responses
4. **sellerorderget.py**
    - Retrieves details of a specific seller order
    - Uses the alibaba.seller.order.get API method
    - Requires an e_trade_id (order ID) as a command-line argument
5. **sellerorderfundget.py**
    - Retrieves fund information for a specific seller order
    - Uses the alibaba.seller.order.fund.get API method
    - Requires an e_trade_id (order ID) as a command-line argument
6. **sellerorderlogisticsget.py**
    - Retrieves logistics information for a specific seller order
    - Uses the alibaba.seller.order.logistics.get API method
    - Requires an e_trade_id (order ID) as a command-line argument
7. **sellerordershipping.py**
    - Updates shipping information for a specific order
    - Uses the alibaba.seller.order.shipping API method
    - Requires multiple command-line arguments for shipping details
## Usage
1. Run `1initiate.py`  to start the authorization process and obtain the AUTH_CODE.
2. Run `2createtoken.py`  to generate the access token (SESSION_KEY).
3. Use the other scripts as needed to interact with seller order data.
Examples:

```bash
python sellerorderget.py <e_trade_id>
python sellerorderfundget.py <e_trade_id>
python sellerorderlogisticsget.py <e_trade_id>
python sellerordershipping.py <service_provider> <trade_id> <logistics_type> <tracking_number> <attachments_json>
```
## Logging
All API requests and responses are logged in the `api_logs/` directory for debugging and auditing purposes.

## Disclaimer
This project is for educational and integration purposes only. Ensure you have the necessary permissions and comply with Alibaba's terms of service when using these scripts. The authors are not responsible for any misuse or damage caused by this project.

This updated README now includes the detailed Scripts Overview section and retains the Logging section. It provides a comprehensive guide to the project, its scripts, setup process, and usage instructions.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Alibaba Seller API Integration Flowchart-1.eraserdiagram" data-element-id="CIQeV1CwC1eI5bC16W0Qb"><img src="/.eraser/o8hc74AnQrLKcf0ufzUD___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----a7c8b791fff47f62f024852ab8b4a50e-Alibaba-Seller-API-Integration-Flowchart.png" alt="" data-element-id="CIQeV1CwC1eI5bC16W0Qb" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/o8hc74AnQrLKcf0ufzUD --->