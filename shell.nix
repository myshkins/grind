let
  pkgs = import <nixpkgs> {};
  go = pkgs.go;
  gopls = pkgs.gopls;
  pythonEnv = (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas
      python-pkgs.requests
    ]));

in pkgs.mkShell {
  packages = [
    pythonEnv
    go
    gopls
  ];

  }
