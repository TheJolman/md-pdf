{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        lib = nixpkgs.lib;
        pkgs = nixpkgs.legacyPackages.${system};

      in {
        packages.default = pkgs.python3Packages.buildPythonPackage {
          name = "md-pdf";
          version = "0.1.0";
          src = ./.;
          pyproject = true;

          build-system = with pkgs.python3Packages; [
            hatchling
          ];

          dependencies = with pkgs.python3Packages; [
            markdown
            weasyprint
          ];
        };
      }
    );
}
