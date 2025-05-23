{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        # lib = nixpkgs.lib;
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python313Packages;

        md-pdf = python.buildPythonPackage {
          name = "md-pdf";
          version = "0.1.0";
          src = ./.;
          pyproject = true;

          build-system = with python; [
            hatchling
          ];

          dependencies = with python; [
            markdown
            weasyprint
          ];
        };
      in {
        packages.default = md-pdf;
        apps.default = {
          type = "app";
          program = "${md-pdf}/bin/md-pdf";
        };
      }
    );
}
