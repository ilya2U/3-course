import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { useState } from "react";
import { TextField, Typography } from "@mui/material";

const App = () => {
  const [selectedData, setSelectedData] = useState([]);
  const [name, setName] = useState("");
  const [replay, setReplay] = useState(false);
  const [registerName, setRegisterName] = useState([]);
  const [isRegister, setIsRegister] = useState(false);
  const [isLogin, setIsLogin] = useState("");
  const [tryes, setTryes] = useState(0);
  const [error, setError] = useState("");
  const [bannList, setBanList] = useState([]);

  const switchData = (num) => {
    if (!selectedData.includes(num)) {
      setSelectedData([...selectedData, num]);
    }
  };

  const start = () => {
    if (registerName.find((el) => el.name === name)) {
      const people = registerName.find((el) => el.name === name);
      if (tryes !== 3) {
        if (people.code === JSON.stringify(selectedData)) {
          setIsLogin(true);
          setSelectedData([]);
          setIsLogin(name);
          setName("");
          setIsRegister(false);
          setError("");
          setTryes(0);
        } else {
          setTryes(tryes + 1);
          setSelectedData([]);
          setIsRegister(false);
          setError("Не верный ключ");
          setIsLogin("");
        }
      } else {
        setBanList([...bannList, name]);
      }
    } else {
      if (replay.replay === true) {
        if (replay.code === JSON.stringify(selectedData)) {
          setReplay({ replay: false, code: "" });
          setRegisterName([
            ...registerName,
            { name, code: JSON.stringify(selectedData) },
          ]);
          setName("");
          setSelectedData([]);
          setIsRegister(true);
          setError("");
        } else {
          setSelectedData([]);
          setError(
            "Неверное повторение пароля, повторите попытку или начните регистрацию заново "
          );
          console.log(replay);
        }
      } else {
        setReplay({ replay: true, code: JSON.stringify(selectedData) });
        setSelectedData([]);
        setIsRegister(false);
        setIsLogin("");
        setError("");
        setTryes(0);
      }
    }
  };

  const close = () => {
    setSelectedData([]);
    setName("");
    setReplay({ replay: false, code: "" });
    setIsRegister(false);
    setIsLogin("");
    setTryes(0);
    setError("");
  };

  return (
    <Box
      sx={{
        width: "100%",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Box
        sx={{
          width: "1000px",
          display: "flex",
          gap: "40px",
        }}
        fullWidth
      >
        <Box width="400px">
          <TextField
            placeholder="Имя"
            value={name}
            fullWidth
            onChange={(e) => setName(e.target.value)}
            sx={{ mb: "30px" }}
            disabled={replay.replay}
          />
          <Box sx={{ display: "flex", justifyContent: "space-between" }}>
            <Button
              disabled={
                !name || !selectedData.length || bannList.includes(name)
              }
              variant="contained"
              onClick={() => start()}
            >
              Начать
            </Button>
            <Button variant="contained" onClick={() => close()}>
              Отменить
            </Button>
          </Box>
          <Box sx={{ mt: "30px" }}>
            {replay.replay && <Typography>Повторите ввод еще раз</Typography>}
            {isRegister && (
              <Typography>Успешная регистрация пользователя</Typography>
            )}
            {isLogin && (
              <Typography>Пользователь {isLogin} успешно зашел</Typography>
            )}
            {error && <Typography>{error}</Typography>}
            {tryes !== 0 && (
              <Typography>Попыток осталось {3 - tryes}</Typography>
            )}
            {bannList.includes(name) && (
              <Typography>Пользователь {name} заблокирован</Typography>
            )}
          </Box>
        </Box>

        <Box width="600px">
          <Button
            sx={{ mb: "30px" }}
            onClick={() => setSelectedData([])}
            variant="contained"
          >
            Очистить
          </Button>

          <table
            style={{
              width: "600px",
              borderSpacing: "0px 0 px",
              height: "600px",
              borderCollapse: "collapse",
            }}
          >
            <tr>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("1")}
                  className={`myButton ${
                    selectedData.includes("1") && "selected"
                  }`}
                ></button>
              </td>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("2")}
                  className={`myButton ${
                    selectedData.includes("2") && "selected"
                  }`}
                ></button>
              </td>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("3")}
                  className={`myButton ${
                    selectedData.includes("3") && "selected"
                  }`}
                ></button>
              </td>
            </tr>
            <tr>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("4")}
                  className={`myButton ${
                    selectedData.includes("4") && "selected"
                  }`}
                ></button>
              </td>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("5")}
                  className={`myButton ${
                    selectedData.includes("5") && "selected"
                  }`}
                ></button>
              </td>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("6")}
                  className={`myButton ${
                    selectedData.includes("6") && "selected"
                  }`}
                ></button>
              </td>
            </tr>
            <tr>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("7")}
                  className={`myButton ${
                    selectedData.includes("7") && "selected"
                  }`}
                ></button>
              </td>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("8")}
                  className={`myButton ${
                    selectedData.includes("8") && "selected"
                  }`}
                ></button>
              </td>
              <td style={{ border: "3px solid black", padding: "0px" }}>
                <button
                  onClick={() => switchData("9")}
                  className={`myButton ${
                    selectedData.includes("9") && "selected"
                  }`}
                ></button>
              </td>
            </tr>
          </table>
        </Box>
      </Box>
    </Box>
  );
};

export default App;
