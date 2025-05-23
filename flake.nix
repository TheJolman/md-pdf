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
        # lib = nixpkgs.lib;
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = "python313Packages";

      in {
        packages.default = pkgs.${pythonPackages}.buildPythonPackage {
          name = "md-pdf";
          version = "0.1.0";
          src = ./.;
          pyproject = true;

          build-system = with pkgs.${pythonPackages}; [
            hatchling
          ];

          dependencies = with pkgs.${pythonPackages}; [
            markdown
            weasyprint
          ];
        };
      }
    );
}
