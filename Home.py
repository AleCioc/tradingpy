import streamlit as st

# HTML code for the TradingView widget
# You might need to adjust the "symbol" and other parameters as needed.
tradingview_html = """
<div class="tradingview-widget-container">
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": false,
  "width": "980",
  "height": "610",
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_widget"
  }
  );
  </script>
</div>
"""


def main():
    st.title('TradingView Widget in Streamlit')

    # Using components.html to embed the TradingView HTML code
    st.components.v1.html(tradingview_html, height=1000)


if __name__ == "__main__":
    main()
