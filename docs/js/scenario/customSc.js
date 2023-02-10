document.querySelectorAll(".use-termynalSc").forEach((node) => {
  node.style.display = "block";
  new TermynalScenario(node, {
    lineDelay: 500,
  });
});
const progressLiteralStartSc = "---> 100%";
const promptLiteralStartSc = "$ ";
const customPromptLiteralStartSc = "# ";
const termynalActivateClassSc = "termyScenario";
let termynalsSc = [];

function createTermynalScenario() {
  document
    .querySelectorAll(`.${termynalActivateClassSc} .highlight`)
    .forEach((node) => {
      const text = node.textContent;
      const lines = text.split("\n");
      const useLines = [];
      let buffer = [];
      function saveBuffer() {
        if (buffer.length) {
          let isBlankSpace = true;
          buffer.forEach((line) => {
            if (line) {
              isBlankSpace = false;
            }
          });
          dataValue = {};
          if (isBlankSpace) {
            dataValue["delay"] = 0;
          }
          if (buffer[buffer.length - 1] === "") {
            // A last single <br> won't have effect
            // so put an additional one
            buffer.push("");
          }
          const bufferValue = buffer.join("<br>");
          dataValue["value"] = bufferValue;
          useLines.push(dataValue);
          buffer = [];
        }
      }
      for (let line of lines) {
        if (line === progressLiteralStartSc) {
          saveBuffer();
          useLines.push({
            type: "progress",
          });
        } else if (line.startsWith(promptLiteralStartSc)) {
          saveBuffer();
          const value = line.replace(promptLiteralStartSc, "").trimEnd();
          useLines.push({
            type: "input",
            value: value,
          });
        } else if (line.startsWith("// ")) {
          saveBuffer();
          const value = "💬 " + line.replace("// ", "").trimEnd();
          useLines.push({
            value: value,
            class: "termynal-commentSc",
            delay: 0,
          });
        } else if (line.startsWith(customPromptLiteralStartSc)) {
          saveBuffer();
          const promptStart = line.indexOf(promptLiteralStartSc);
          if (promptStart === -1) {
            console.error("Custom prompt found but no end delimiter", line);
          }
          const prompt = line
            .slice(0, promptStart)
            .replace(customPromptLiteralStartSc, "");
          let value = line.slice(promptStart + promptLiteralStartSc.length);
          useLines.push({
            type: "input",
            value: value,
            prompt: prompt,
          });
        } else {
          buffer.push(line);
        }
      }
      saveBuffer();
      const div = document.createElement("div");
      node.replaceWith(div);
      const termynal = new TermynalScenario(div, {
        lineData: useLines,
        noInit: true,
        lineDelay: 500,
      });
      termynalsSc.push(termynal);
    });
}

function loadVisibleTermynals() {
  termynalsSc = termynalsSc.filter((termynal) => {
    if (termynal.container.getBoundingClientRect().top - innerHeight <= 0) {
      termynal.init();
      return false;
    }
    return true;
  });
}
window.addEventListener("scroll", loadVisibleTermynals);
createTermynalScenario();
loadVisibleTermynals();
