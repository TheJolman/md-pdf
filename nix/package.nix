{
  buildPythonPackage,
  hatchling,
  markdown,
  weasyprint,
  lib,
}:
buildPythonPackage {
  pname = "md-pdf";
  version = "0.1.0";
  pyproject = true;
  src = ./..;

  build-system = [
    hatchling
  ];

  dependencies = [
    markdown
    weasyprint
  ];

  meta = with lib; {
    description = "md to pdf converter";
    homepage = "https://github.com/thejolman/md-pdf";
    license = licenses.mit;
    maintainers = with maintainers; [TheJolman];
    mainProgram = "md-pdf";
  };
}
