
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    category = "calculator"

    if request.method == "POST":
        category = request.form.get("category", "calculator")

        try:
            if category == "calculator":
                a = float(request.form.get("number1", ""))
                b = float(request.form.get("number2", ""))
                operation = request.form.get("operation", "+")

                if operation == "+":
                    result = a + b
                elif operation == "-":
                    result = a - b
                elif operation == "*":
                    result = a * b
                elif operation == "/":
                    if b == 0:
                        raise ValueError("Cannot divide by zero!")
                    result = a / b
                else:
                    raise ValueError("Invalid operation.")

            elif category == "unit":
                value = float(request.form.get("value", ""))
                conversion = request.form.get("conversion", "")

                if conversion == "km_miles":
                    result = f"{value * 0.621371:.2f} miles"
                elif conversion == "c_f":
                    result = f"{(value * 9 / 5) + 32:.2f} °F"
                else:
                    raise ValueError("Please select a valid conversion.")

            elif category == "currency":
                amount = float(request.form.get("amount", ""))
                conversion = request.form.get("currency_conversion", "")

                if amount < 0:
                    raise ValueError("Amount cannot be negative.")

                # Example rate only; not a live exchange rate.
                inr_per_usd = 83.0

                if conversion == "inr_usd":
                    result = f"${amount / inr_per_usd:.2f} USD"
                elif conversion == "usd_inr":
                    result = f"₹{amount * inr_per_usd:.2f} INR"
                else:
                    raise ValueError("Please select a currency conversion.")

            else:
                raise ValueError("Invalid calculator category.")

        except ValueError as exc:
            error = str(exc) if str(exc) in [
                "Cannot divide by zero!",
                "Amount cannot be negative.",
                "Invalid operation.",
                "Please select a valid conversion.",
                "Please select a currency conversion.",
                "Invalid calculator category."
            ] else "Please enter valid numbers in all required fields."

    return render_template(
        "index.html",
        result=result,
        error=error,
        category=category
    )


if __name__ == "__main__":
    app.run(debug=True)
