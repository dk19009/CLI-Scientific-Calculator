import sympy as sp

def main():
    # Enabling pretty-printing
    sp.init_printing(unicode=True)

    # Setting default mode to radians
    mode = "rad"

    # Defining additional inverse and reciprocal functions
    sp.sech = lambda x: 1 / sp.cosh(x)
    sp.csch = lambda x: 1 / sp.sinh(x)
    sp.coth = lambda x: 1 / sp.tanh(x)
    sp.asech = lambda x: sp.acosh(1 / x)
    sp.acsch = lambda x: sp.asinh(1 / x)
    sp.acoth = lambda x: sp.atanh(1 / x)

    # Convenience shortcuts
    cbrt = lambda x: sp.root(x, 3)
    fourth_root = lambda x: sp.root(x, 4)
    fifth_root = lambda x: sp.root(x, 5)
    log2 = lambda x: sp.log(x, 2)
    logb = lambda x, b: sp.log(x, b)
    perm = lambda n, r: sp.factorial(n) / sp.factorial(n - r)
    comb = lambda n, r: sp.factorial(n) / (sp.factorial(r) * sp.factorial(n - r))

    # Additional constants
    phi = (1 + sp.sqrt(5)) / 2 # Golden Ratio
    tau = 2 * sp.pi # Ratio of a circle's circumference to its radius

    # Define default symbols
    x, y, z = sp.symbols('x y z')

    # Storing previous answers
    ans = []

    print("🖩 Welcome to my Scientific Calculator! 🖩")
    print("Suppords: trigonometric functions, logarithms, roots, combinatorics, and constants.")
    print("Try: sin(x), log(x), root(x, n), comb(n, r), perm(n, r), pi, e, tau, phi")
    print("Commands: mode rad | mode deg | clear | history | help | exit\n")

    while True:
        cmd = input(">>> ").strip().lower()
        if not cmd: 
            continue # Re-prompts the user for an input
        elif cmd in {'exit', 'quit'}:
            break # Exits program
        elif cmd.startswith("mode "):
            new_mode = cmd.split()[1]
            if new_mode in {'deg', 'rad'}:
                mode = new_mode # Changes mode accordingly
                print(f"✅ Mode switched to {mode}")
            else:
                print("❌ Use 'mode deg' or 'mode rad'") # Error message for invalid mode
            continue # Re-prompts the user after changing the mode
        elif cmd in {"help", "?"}:
            # Help Section
            print("""📖 Help:
                ▶ trig: sin(x), cos(x), tan(x), etc.
                ▶ log: log(x), logb(x, base), log2(x)
                ▶ roots: root(x, n), cbrt(x), fourth_root(x)
                ▶ combinatorics: comb(n, r), perm(n, r)
                ▶ constants: pi, e, tau, phi
                ▶ previous answer: ans
                ▶ commands: mode deg | mode rad | history | clear | help | exit
                ▶ use 'ans' to reuse last result""")
            continue
        elif cmd == "ans":
            print("Last answer: ", ans[-1] if ans else 'No previous calculations found.')
            continue
        elif cmd == "history":
            for i, val in enumerate(ans, 1):
                print(f"[{i}] = {val}")
            continue
        elif cmd == "clear":
            ans.clear()
            print("✅ Memory cleared.")
            continue

        # Replace 'ans' with the last computed value (if exists)
        if "ans" in cmd:
            if ans:
                cmd = cmd.replace("ans", str(ans[-1]))
            else:
                print("⚠️ Error: No previous answer available.")
                continue

        try:
            expr = sp.sympify(cmd, locals=locals(), evaluate=True)

            if mode == "deg":
                deg_to_rad = sp.pi / 180

                # Converting arguments in the trig functions to their degree equivalents
                expr = \
                    expr.replace(sp.sin, lambda x: sp.sin(x * deg_to_rad)) \
                        .replace(sp.cos, lambda x: sp.cos(x * deg_to_rad)) \
                        .replace(sp.tan, lambda x: sp.tan(x * deg_to_rad)) \
                        .replace(sp.sec, lambda x: sp.sec(x * deg_to_rad)) \
                        .replace(sp.csc, lambda x: sp.csc(x * deg_to_rad)) \
                        .replace(sp.cot, lambda x: sp.cot(x * deg_to_rad)) \
                        .replace(sp.asin, lambda x: sp.asin(x * deg_to_rad)) \
                        .replace(sp.acos, lambda x: sp.acos(x * deg_to_rad)) \
                        .replace(sp.atan, lambda x: sp.atan(x * deg_to_rad)) \
                        .replace(sp.asec, lambda x: sp.asec(x * deg_to_rad)) \
                        .replace(sp.acsc, lambda x: sp.acsc(x * deg_to_rad)) \
                        .replace(sp.sinh, lambda x: sp.sinh(x * deg_to_rad)) \
                        .replace(sp.cosh, lambda x: sp.cosh(x * deg_to_rad)) \
                        .replace(sp.tanh, lambda x: sp.tanh(x * deg_to_rad)) \
                        .replace(sp.sech, lambda x: sp.sech(x * deg_to_rad)) \
                        .replace(sp.csch, lambda x: sp.csch(x * deg_to_rad)) \
                        .replace(sp.asinh, lambda x: sp.asinh(x * deg_to_rad)) \
                        .replace(sp.acosh, lambda x: sp.acosh(x * deg_to_rad)) \
                        .replace(sp.atanh, lambda x: sp.atanh(x * deg_to_rad)) \
                        .replace(sp.asech, lambda x: sp.asech(x * deg_to_rad)) \
                        .replace(sp.acsch, lambda x: sp.acsch(x * deg_to_rad)) \
                        .replace(sp.acoth, lambda x: sp.acoth(x * deg_to_rad))

            result = expr.evalf()
            print("= ", expr)
            print("= ", result)
            ans.append(result)
            print("Last Answer: ", ans[-1] if ans else "No previous answer") 

        except ZeroDivisionError:
            print("⚠️ Division by zero is undefined.")
        except ValueError as ve:
            print("⚠️ Math domain error:", ve)
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    main()